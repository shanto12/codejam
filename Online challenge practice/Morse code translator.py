input_text = "SOSsdfsdfasdf"
expected_output = "... --- ... ... -.. ..-. ... -.. ..-. .- ... -.. ..-."
morse_code = ""

text = """A	.-	B	-...	C	-.-.	D	-..	E	.	F	..-.
G	--.	H	....	I	..	J	.---	K	-.-	L	.-..
M	--	N	-.	O	---	P	.--.	Q	--.-	R	.-.
S	...	T	-	U	..-	V	...-	W	.--	X	-..-
Y	-.--	Z	--.. 0	-----	1	.----	2	..---	3	...--	4	....-	5	.....
6	-....	7	--...	8	---..	9	----. .	.-.-.-	,	--..--	?	..--..	'	.----.	!	-.-.--	/	-..-.
(	-.--.	)	-.--.-	&	.-...	:	---...	;	-.-.-.	=	-...-
+	.-.-.	-	-....-	_	..--.-	"	.-..-.	$	...-..-	@	.--.-.
¿	..-.-	¡	--...-"""

text_list = text.split()
key = ""
flag = False
morse_map_dict = dict()
for i, text in enumerate(text_list):
    if flag:
        morse_map_dict[key] = text
    else:
        key = text
    flag = not flag
    print(i, text)



morse_code += " ".join(morse_map_dict[char.upper()] for char in input_text)

if morse_code == expected_output:
    print("GOOD")
else:
    print("BAD")
print(morse_code)
