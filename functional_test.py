import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(3)
    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #* 철수는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고 해당 웹 사이트를 확인하러 간다.
        self.browser.get("http://localhost:8000")

        #* 웹 페이지 타이틀과 해더가 'TO-DO'를 효시하고 있다.
        self.assertIn('TO-DO', self.browser.title)
        self.fail('finish the test!')

    """
    그는 바로 작업을 추가하기로 한다.
    "공작깃털 사기"라고 텍스트 상자에 입력한다.
    
    엔터키를 치면 페이지가 갱신되고 작업목록에
    "1: 공작깃털 사기" 아이템이 추가된다.
    
    추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
    다시 "공작 깃털을 이용해서 그물 만들기"라고 입력한다.
    
    페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다
    철수는 사이트가 입력한 목록을 저장하고 있는지 궁금하다
    사이트는 그를 위핸 특정 URL을 생성해준다
    이때 URL에 대한 설명도 함께 제공된다.
    
    해당 URL에 접속하면 그가 만든 작업 목록이 그대로 있는 것을 확인할 수 있다.
    
    만족하고 잠자리에 든다
    """


if __name__ == '__main__':
    unittest.main(warnings='ignore')