from django import forms

COLOR_CHOICES = (
	('0', 'BLACK'),
	('1', 'BROWN'),
	('2', 'RED'),
	('3', 'ORANGE'),
	('4', 'YELLOW'),
	('5', 'GREEN'),
	('6', 'BLUE'),
	('7', 'VIOLET'),
	('8', 'GREY'),
	('9', 'WHITE'),
)

TOLERANCE_CHOICES = (
	('5', 'GOLD'),
	('10', 'SILVER'),

	)


class ColorCodeForm(forms.Form):
	band1 = forms.ChoiceField(choices = COLOR_CHOICES)
	band2 = forms.ChoiceField(choices = COLOR_CHOICES)
	band3 = forms.ChoiceField(choices = COLOR_CHOICES)
	tolerance = forms.ChoiceField(choices = TOLERANCE_CHOICES)

