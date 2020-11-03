from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve
import re
from lists.views import home_page


class HomePageTest(TestCase):
    def remove_csrf(self, origin):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', origin)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = self.remove_csrf(render_to_string('home.html', request=request))
        response_decode = self.remove_csrf(response.content.decode())
        self.assertEqual(response_decode, expected_html)

    def test_home_page_can_save_a_POST_request(self):
        # * post 요청 처리와 반환된 html이 신규 아이템 텍스트를 포함하는지 확인
        # * Setup
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'
        # * Exercise
        response = home_page(request)
        # * Assertion
        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = self.remove_csrf(render_to_string(
                        'home.html', {'new_item_text': '신규 작업 아이템'}))
        response_decode = self.remove_csrf(response.content.decode())
        self.assertEqual(response_decode, expected_html)