
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class APIRootTest(APITestCase):
	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class UsersTest(APITestCase):
	def test_users_list(self):
		response = self.client.get('/api/users/')
		self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])

class TeamsTest(APITestCase):
	def test_teams_list(self):
		response = self.client.get('/api/teams/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivitiesTest(APITestCase):
	def test_activities_list(self):
		response = self.client.get('/api/activities/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardTest(APITestCase):
	def test_leaderboard_list(self):
		response = self.client.get('/api/leaderboard/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutsTest(APITestCase):
	def test_workouts_list(self):
		response = self.client.get('/api/workouts/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
