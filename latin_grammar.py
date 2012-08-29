conjugations = ['am', 'amini', 'amur', 'amus', 'ant', 'antur', 'ar', 'aris', 'as', 'at', 'atis', 'atur', 'bam', 'bamini', 'bamur', 'bamus', 'bant', 'bantur', 'bar', 'baris', 'bas', 'bat', 'batis', 'batur', 'beris', 'bimini', 'bimur', 'bimus', 'bis', 'bit', 'bitis', 'bitur', 'bo', 'bor', 'bunt', 'buntur', 'ebam', 'ebamini', 'ebamur', 'ebamus', 'ebant', 'ebantur', 'ebar', 'ebaris', 'ebas', 'ebat', 'ebatis', 'ebatur', 'em', 'emini', 'emur', 'emus', 'ent', 'entur', 'er', 'erim', 'erimus', 'erint', 'eris', 'erit', 'eritis', 'ero', 'erunt', 'es', 'et', 'etis', 'etur', 'i', 'iam', 'iamini', 'iamur', 'iamus', 'iant', 'iantur', 'iar', 'iaris', 'ias', 'iat', 'iatis', 'iatur', 'iebam', 'iebamini', 'iebamur', 'iebamus', 'iebant', 'iebantur', 'iebar', 'iebaris', 'iebas', 'iebat', 'iebatis', 'iebatur', 'iemini', 'iemur', 'iemus', 'ient', 'ientur', 'ieris', 'ies', 'iet', 'ietis', 'ietur', 'imini', 'imur', 'imus', 'io', 'ior', 'is', 'isti', 'istis', 'it', 'itis', 'itur', 'iunt', 'iuntur', 'm', 'mini', 'mur', 'mus', 'nt', 'ntur', 'o', 'or', 'r', 'ris', 's', 't', 'tis', 'tur', 'unt', 'untur', 'verunt']
declinations = ['a', 'ae', 'am', 'arum', 'as', 'e', 'ebus', 'ei', 'em', 'erum', 'es', 'i', 'ia', 'ibus', 'im', 'is', 'ium', 'o', 'orum', 'os', 's', 'u', 'ui', 'um', 'us', 'uum']

def conjugate(base):
	return set([base + conjugation for conjugation in conjugations])

def declinate(base):
	return set([base + declination for declination in declinations])
