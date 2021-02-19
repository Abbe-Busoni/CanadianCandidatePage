from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, views, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, CandidateSerializer
import pandas as pd
import numpy as np

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CandidateView(views.APIView):
    def get(self, request):
        # Read the csv as a pandas dataframe
        df = pd.read_csv('./Canadian Candidates Social Media Ad Spend.csv')
        df = df.replace({np.nan: None})
        # Convert first letter of all Riding values to uppercase
        df['Riding'] = list(map(lambda x: x.title(), df['Riding']))
        candidates = df.to_dict('records')
        #candidates = [ { 'name': 'Ghada Alatrash', 'party': 'Liberal', 'riding': 'CALGARY SIGNAL HILL', 'facebook_page': '',  'twitter_handle': 'ghadaalatrash', 'facebook_spending': 684, 'twitter_spending': 5172 } ]
        
        # Serialize the data using the rules specified in the serialization class
        serialized_data = CandidateSerializer(candidates, many=True)
        return Response(serialized_data.data)

class PartyView(views.APIView):
    def get(self, request):
        df = pd.read_csv('./Canadian Candidates Social Media Ad Spend.csv')
        df = df.replace({np.nan: None})
        # Calculate the total spent by the candidate
        df['total'] = df['Facebook Spend'] + df['Twitter Spend']
        # Group By 'Party' and aggregate the data by the specified values
        insights = df.groupby(['Party'])[['total']].agg([ 'count', 'mean', 'median', 'sum', ])
        # Rename the columns so they're not tuples
        insights.columns = [ 'count', 'mean', 'median', 'sum' ]
        # Converts the df to list of tuples: [ (party_name, {'key': 'value'}), ... ]
        data = list(zip(insights.index, insights.to_dict('records')))
        return Response({'data': data})
