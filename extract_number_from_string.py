text = "X-DSPAM-Confidence:    0.8475"
ind=text.find('0')
extr=text[ind:]
print(float(extr))
