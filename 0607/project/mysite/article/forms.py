from django import forms
from article.models import Article

class ArticleForm(forms.ModelForm):
	title = forms.CharField(label='食譜名稱', max_length=128)
	content = forms.CharField(label='想先說些什麼呢？',widget= forms.Textarea)
	videoID= forms.CharField(label='Youtube影片ID', widget= forms.TextInput)
	material= forms.CharField(label='材料', widget=forms.Textarea)
	step1 = forms.CharField(label='做法', widget=forms.Textarea )
	# author = forms.CharField(label='作者', initial="{{request.user}}")


	class Meta:
		model = Article
		fields = ['title','content','videoID','material','step1']
		#exclude =['author']