from django.test import TestCase
from CTList.views import MainPage
from CTList.models import User


class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'mainpage.html')
        
    def test_responding_POST_request(self):
        resp = self.client.post('/', data={'for1Form': 'Clyde', 'for2Form': '84', 'for3Form': 'the ting go skra', 'game1': 'Strongly Agree', 'game2': 'Agree', 'game3': 'Neutral'})

        self.assertEqual(User.objects.count(), 1)
        brandy = User.objects.first()
        self.assertEqual(brandy.name, 'Clyde')
        self.assertEqual(brandy.number, '84')
        self.assertEqual(brandy.comment, 'the ting go skra')
        self.assertEqual(brandy.question1, 'Strongly Agree')
        self.assertEqual(brandy.question2, 'Agree')
        self.assertEqual(brandy.question3, 'Neutral')

    def test_POST_redirect(self):
        response = self.client.post('/', data={'for1Form': 'Clyde', 'for2Form': '84', 'for3Form': 'the ting go skra', 'game1': 'Strongly Agree', 'game2': 'Agree', 'game3': 'Neutral'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_if_necessary(self):
        self.client.get('/')
        self.assertEqual(User.objects.count(), 0)

    class ORMTest(TestCase):
        def test_saving_retrieving_list(self):
            txtItem1 = User()
            txtItem1.name = 'Clyde'
            txtItem1.number = '84'
            txtItem1.comment = 'the ting go skra'
            txtItem1.question1 = 'Strongly Agree'
            txtItem1.question2 = 'Agree'
            txtItem1.question3 = 'Neutral'
            txtItem1.save()
            txtItem2 = User()
            txtItem2.name = 'Agnes'
            txtItem2.number = '69'
            txtItem2.comment = 'super idol'
            txtItem2.question1 = 'Strongly Disagree'
            txtItem2.question2 = 'Neutraler'
            txtItem2.question3 = 'Disagree'
            txtItem2.save()
            itemsSaved = User.objects.all()
            self.assertEqual(itemsSaved.count(), 2)
            itemsSaved1 = itemsSaved[0]
            itemsSaved2 = itemsSaved[1]
            self.assertEqual(itemsSaved1.name, 'Clyde')
            self.assertEqual(itemsSaved1.number, '84')
            self.assertEqual(itemsSaved1.comment, 'the ting go skra')
            self.assertEqual(itemsSaved1.question1, 'Strongly Agree')
            self.assertEqual(itemsSaved1.question2, 'Agree')
            self.assertEqual(itemsSaved1.question3, 'Neutral')
            self.assertEqual(itemsSaved2.name, 'Agnes')
            self.assertEqual(itemsSaved2.number, '69')
            self.assertEqual(itemsSaved2.comment, 'super idol')
            self.assertEqual(itemsSaved2.question1, 'Strongly Disagree')
            self.assertEqual(itemsSaved2.question2, 'Neutraler')
            self.assertEqual(itemsSaved2.question3, 'Disagree')

        def test_saving_retrieving_list(self):
            User.objects.create(name='Clyde',
            number='84',
            comment='the thing go skra',
            question1='Strongly Agree',
            question2='Agree',
            question3='Neutral')

            User.objects.create(name='Agnes',
            number='69',
            comment='super idol',
            question1='Strongly Disagree',
            question2='Neutraler',
            question3='Disagree')

            response = self.client.get('/')
            self.assertIn('1: Justin, 1, Super Idol, Agree, Disagree, Neutral', response.content.decode())
        # self.assertIn('postName', resp.content.decode())
        # self.assertIn('postNumber', resp.content.decode())
        # self.assertIn('postParagraph', resp.content.decode())

        # self.assertTemplateUsed(resp, 'mainpage.html')

# Create your tests here.
