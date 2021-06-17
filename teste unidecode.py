import unidecode
accented_string = u'Málaga'
# accented_string is of type 'unicode'

unaccented_string = unidecode.unidecode(accented_string)
# unaccented_string contains 'Malaga'and is of type 'str'

print(unaccented_string)