from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question #사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성
        '''
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': "form-control", 'rows': 10}),
        }
        {{ form.as_p }}을 이용하면 빠르게 템플릿을 만들 수 있지만 HTML 코드가 자동 생성되어 제한이 생김
        -> 폼을 이용하여 자동으로 HTML 코드를 생성하지 말고 직접 HTML 코드는 작성하는 방법 사용
        '''
        
        
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '답변내용',
        }