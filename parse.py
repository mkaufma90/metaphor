import xml.etree.ElementTree as etree
import re


def extract_texts(corpus):

	fict = ["ab9-fragment03", "ac2-fragment06", "bmw-fragment09", "bpa-fragment14", "c8t-fragment01", "cb5-fragment02", "ccw-fragment03", "ccw-fragment04", "cdb-fragment02", "cdb-fragment04", "faj-fragment17", "fet-fragment01", "fpb-fragment01", "g0l-fragment01"]
	aca = ["acj-fragment01", "alp-fragment01", "amm-fragment02", "as6-fragment01", "as6-fragment02", "b17-fragment02", "b1g-fragment02", "clp-fragment01", "clw-fragment01", "crs-fragment01", "cty-fragment03", "ea7-fragment03", "ecv-fragment05", "ew1-fragment01", "fef-fragment03"]
	conv = ["kb7-fragment10", "kb7-fragment31", "kb7-fragment45", "kb7-fragment48", "kbc-fragment13", "kbd-fragment07", "kbd-fragment21", "kbh-fragment01", "kbh-fragment02", "kbh-fragment03", "kbh-fragment04", "kbh-fragment09", "kbh-fragment41", "kbj-fragment17", "kbp-fragment09", "kbw-fragment04", "kbw-fragment09", "kbw-fragment11", "kbw-fragment17", "kbw-fragment42", "kcc-fragment02", "kcf-fragment14", "kcu-fragment02", "kcv-fragment42"];
	news = ["a1e-fragment01", "a1f-fragment06", "a1f-fragment07", "a1f-fragment08", "a1f-fragment09", "a1f-fragment10", "a1f-fragment11", "a1f-fragment12", "a1g-fragment26", "a1g-fragment27", "a1h-fragment05", "a1h-fragment06", "a1j-fragment33", "a1j-fragment34", "a1k-fragment02", "a1l-fragment01", "a1m-fragment01", "a1n-fragment09", "a1n-fragment18", "a1p-fragment01", "a1p-fragment03", "a1u-fragment04", "a1x-fragment03", "a1x-fragment04", "a1x-fragment05", "a2d-fragment05", "a31-fragment03", "a36-fragment07", "a38-fragment01", "a39-fragment01", "a3c-fragment05", "a3e-fragment02", "a3e-fragment03", "a3k-fragment11", "a3m-fragment02", "a3p-fragment09", "a4d-fragment02", "a5e-fragment06", "a6u-fragment02", "a7s-fragment03", "a7t-fragment01", "a7w-fragment01", "a7y-fragment03", "a80-fragment15", "a8m-fragment02", "a8n-fragment19", "a8r-fragment02", "a8u-fragment14", "a98-fragment03", "a9j-fragment01", "aa3-fragment08", "ahb-fragment51", "ahc-fragment60", "ahc-fragment61", "ahd-fragment06", "ahe-fragment03", "ahf-fragment24", "ahf-fragment63", "ahl-fragment02", "ajf-fragment07", "al0-fragment06", "al2-fragment16", "al2-fragment23", "al5-fragment03"]

	"""
	Input: name of a corpus file
	Output: l
	ist of individual texts (as xml elements)
	"""
	tree = etree.parse(corpus)

	root = tree.getroot()

	header, text1 = root.getchildren()

	group = text1.getchildren()[0]

	texts = group.getchildren()
	counter = 0
	sentences = []

	for text in texts:
		genre = ""
		fragId = text.attrib['{http://www.w3.org/XML/1998/namespace}id']
		genre = "fict" if fragId in fict else "aca" if fragId in aca else "conv" if fragId in conv else "news" if fragId in news else -1
		for a in text.getchildren()[0].getchildren()[0].getchildren():
			if len(a.getchildren()) > 0:
				for child in a.getchildren():
				 	if child.tag == '{http://www.tei-c.org/ns/1.0}s':
					 	words = []
					 	for w in child.getchildren():
					 		text = w.text
					 		lemma =  w.attrib['lemma'] if 'lemma' in w.attrib.keys() else -1
					 		pType =  w.attrib['type'] if 'type' in w.attrib.keys() else -1
					 		children = w.getchildren()
					 		if len(children) > 0:
				 				attrs = children[0].attrib
				 				text = children[0].text
					 			function =  attrs['function'] if 'function' in attrs.keys() else -1
					 			sType =  attrs['type'] if 'type' in attrs.keys() else -1
					 			morph =  attrs['vici:morph'] if 'vici:morph' in attrs.keys() else -1
			 					words.append((text,lemma,pType, function,sType,morph))
		 					else:
		 						words.append((text,lemma,pType, -1,-1,-1))
					sentences.append((genre,words))


	return sentences


corpus = '2541/VUAMC.xml'
sentences = extract_texts(corpus)
print len(sentences)
for (genre,sentence) in sentences:
	#print genre
	for (text,lemma,pType,function,sType,morph)  in sentence:
		break




    