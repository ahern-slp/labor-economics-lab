def good_skip(year): # use page nums from pdfs for bounds
	# format 1
	if year == '1961':
		l1 = range(11)
		l2 = range(361,425) 
	if year == '1963':
		l1 = range(12)
		l2 = []	
	# format 2: numbered entries
	if year == '1964':
		l1 = range(4)
		l2 = []
	if year == '1965':
		l1 = range(4)
		l2 = range(378,435)
	if year == '1966':
		l1 = range(5)
		l2 = range(408,470)
	if year == '1967':
		l1 = range(4)
		l2 = range(417,485)
	if year == '1968':
		l1 = range(5)
		l2 = range(431,490)
	if year == '1969':
		l1 = range(5)
		l2 = range(435,500)
	if year == '1970':
		l1 = range(5)
		l2 = range(500,570)
	if year == '1971-1972':
		l1 = range(6)
		l2 = range(475,545)
	if year == '1974':
		l1 = range(4)
		l2 = range(395,455)
	if year == '1975':
		l1 = range(4)
		l2 = range(424,490)
	if year == '1976':
		l1 = range(4)
		l2 = range(311,345)
	if year == '1977':
		l1 = range(4)
		l2 = range(216,250)
	if year == '1978':
		l1 = range(4)
		l2 = range(217,250)
	if year == '1979':
		l1 = range(4)
		l2 = range(224,260)
	if year == '1980':
		l1 = range(4)
		l2 = range(229,265)
	if year == '1981':
		l1 = range(4)
		l2 = range(178,215)
	if year == '1982':
		l1 = range(4)
		l2 = range(184,220)
	if year == '1983':
		l1 = range(4)
		l2 = range(182,220)
	if year == '1984':
		l1 = range(4)
		l2 = range(186,225)
	if year == '1985':
		l1 = range(4)
		l2 = range(195,235)
	if year == '1986':
		l1 = range(4)
		l2 = range(198,240)
	if year == '1987':
		l1 = range(4)
		l2 = range(206,250)
	if year == '1988':
		l1 = range(4)
		l2 = range(212,255)
	if year == '1989':
		l1 = range(4)
		l2 = range(251,300)
	if year == '1990':
		l1 = range(5)
		l2 = range(264,320)
	if year == '1991':
		l1 = range(5)
		l2 = range(268,325)
	if year == '1992':
		l1 = range(5)
		l2 = range(277,335)
	if year == '1993':
		l1 = range(5)
		l2 = range(275,325)
	if year == '1994':
		l1 = range(5)
		l2 = range(289,350)
	if year == '1995':
		l1 = range(7)
		l2 = range(311,370)
	if year == '1996':
		l1 = range(5)
		l2 = range(311,370)
	if year == '1997':
		l1 = range(5)
		l2 = range(323,385)
	if year == '1998':
		l1 = range(5)
		l2 = range(336,400)
	if year == '1999':
		l1 = range(5)
		l2 = range(343,405)
	if year == '2000':
		l1 = range(5)
		l2 = range(358,425)
	if year == '2001':
		l1 = range(5)
		l2 = range(380,450)
	if year == '2002':
		l1 = range(5)
		l2 = range(392,460)
	if year == '2003':
		l1 = range(5)
		l2 = range(396,465)
	# format
	if year == '2004':
		l1 = []
		l2 = range(502,610)
	if year == '2005':
		l1 = []
		l2 = range(507,620)
	if year == '2006':
		l1 = []
		l2 = range(522,645)	
		
	return [*l1,*l2]