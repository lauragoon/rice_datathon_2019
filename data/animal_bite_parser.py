def print_gene(data):
	#print(data)
	pos, ref, alt = get_minimal_representation(int(data[1]), str(data[3]), str(data[4]))
	alt = alt.split(',')
	data1 = data[7].split(";")
	#print(data1)


	AC = []
	AF = []
	AC_AFR = []
	AC_AMR = []
	AC_ASJ = []
	AC_EAS = []
	AC_FIN = []
	AC_NFE = []
	AC_OTH = []
	AC_SAS = []
	AC_Male = []
	AC_Female = []
	AN_AFR = []
	AN_AMR = []
	AN_ASJ = []
	AN_EAS = []
	AN_FIN = []
	AN_NFE = []
	AN_OTH = []
	AN_SAS = []
	AN_Male = []
	AN_Female = []
	AF_AFR = []
	AF_AMR = []
	AF_ASJ = []
	AF_EAS = []
	AF_FIN = []
	AF_NFE = []
	AF_OTH = []
	AF_SAS = []
	AF_Male = []
	AF_Female = []
	Hom_AFR = []
	Hom_AMR = []
	Hom_ASJ = []
	Hom_EAS = []
	Hom_FIN = []
	Hom_NFE = []
	Hom_OTH = []
	Hom_SAS = []
	Hom_Male = []
	Hom_Female = []
	Hom = []
	POPMAX = []
	AC_POPMAX = []
	AN_POPMAX = []
	AF_POPMAX = []

	for elem in data1:
		#print("elem:"+elem)
		if elem[:3]=='AC=':
			AC.extend(elem[3:].split(','))
		elif elem[:3]=='AF=':
			AF.extend(elem[3:].split(','))
		elif elem[:7]=='AC_AFR=':
			AC_AFR.extend(elem[7:].split(','))
		elif elem[:7]=='AC_AMR=':
			AC_AMR.extend(elem[7:].split(','))
		elif elem[:7]=='AC_ASJ=':
			AC_ASJ.extend(elem[7:].split(','))
		elif elem[:7]=='AC_EAS=':
			AC_EAS.extend(elem[7:].split(','))
		elif elem[:7]=='AC_FIN=':
			AC_FIN.extend(elem[7:].split(','))
		elif elem[:7]=='AC_NFE=':
			AC_NFE.extend(elem[7:].split(','))
		elif elem[:7]=='AC_OTH=':
			AC_OTH.extend(elem[7:].split(','))
		elif elem[:7]=='AC_SAS=':
			AC_SAS.extend(elem[7:].split(','))
		elif elem[:8]=='AC_Male=':
			AC_Male.extend(elem[8:].split(','))
		elif elem[:10]=='AC_Female=':
			AC_Female.extend(elem[10:].split(','))
		elif elem[:7]=='AN_AFR=':
			AN_AFR.extend(elem[7:].split(','))
		elif elem[:7]=='AN_AMR=':
			AN_AMR.extend(elem[7:].split(','))
		elif elem[:7]=='AN_ASJ=':
			AN_ASJ.extend(elem[7:].split(','))
		elif elem[:7]=='AN_EAS=':
			AN_EAS.extend(elem[7:].split(','))
		elif elem[:7]=='AN_FIN=':
			AN_FIN.extend(elem[7:].split(','))
		elif elem[:7]=='AN_NFE=':
			AN_NFE.extend(elem[7:].split(','))
		elif elem[:7]=='AN_OTH=':
			AN_OTH.extend(elem[7:].split(','))
		elif elem[:7]=='AN_SAS=':
			AN_SAS.extend(elem[7:].split(','))
		elif elem[:8]=='AN_Male=':
			AN_Male.extend(elem[8:].split(','))
		elif elem[:10]=='AN_Female=':
			AN_Female.extend(elem[10:].split(','))
		elif elem[:7]=='AF_AFR=':
			AF_AFR.extend(elem[7:].split(','))
		elif elem[:7]=='AF_AMR=':
			AF_AMR.extend(elem[7:].split(','))
		elif elem[:7]=='AF_ASJ=':
			AF_ASJ.extend(elem[7:].split(','))
		elif elem[:7]=='AF_EAS=':
			AF_EAS.extend(elem[7:].split(','))
		elif elem[:7]=='AF_FIN=':
			AF_FIN.extend(elem[7:].split(','))
		elif elem[:7]=='AF_NFE=':
			AF_NFE.extend(elem[7:].split(','))
		elif elem[:7]=='AF_OTH=':
			AF_OTH.extend(elem[7:].split(','))
		elif elem[:7]=='AF_SAS=':
			AF_SAS.extend(elem[7:].split(','))
		elif elem[:8]=='AF_Male=':
			AF_Male.extend(elem[8:].split(','))
		elif elem[:10]=='AF_Female=':
			AF_Female.extend(elem[10:].split(','))
		elif elem[:8]=='Hom_AFR=':
			Hom_AFR.extend(elem[8:].split(','))
		elif elem[:8]=='Hom_AMR=':
			Hom_AMR.extend(elem[8:].split(','))
		elif elem[:8]=='Hom_ASJ=':
			Hom_ASJ.extend(elem[8:].split(','))
		elif elem[:8]=='Hom_EAS=':
			Hom_EAS.extend(elem[8:].split(','))
		elif elem[:8]=='Hom_FIN=':
			Hom_FIN.extend(elem[8:].split(','))
		elif elem[:8]=='Hom_NFE=':
			Hom_NFE.extend(elem[8:].split(','))
		elif elem[:8]=='Hom_OTH=':
			Hom_OTH.extend(elem[8:].split(','))
		elif elem[:8]=='Hom_SAS=':
			Hom_SAS.extend(elem[8:].split(','))
		elif elem[:9]=='Hom_Male=':
			Hom_Male.extend(elem[9:].split(','))
		elif elem[:11]=='Hom_Female=':
			Hom_Female.extend(elem[11:].split(','))
		elif elem[:4]=='Hom=':
			Hom.extend(elem[4:].split(','))
		elif elem[:7]=='POPMAX=':
			POPMAX.extend(elem[7:].split(','))
		elif elem[:10]=='AC_POPMAX=':
			AC_POPMAX.extend(elem[10:].split(','))
		elif elem[:10]=='AN_POPMAX=':
			AN_POPMAX.extend(elem[10:].split(','))
		elif elem[:10]=='AF_POPMAX=':
			AF_POPMAX.extend(elem[10:].split(','))


	for i in range(len(AC)):
		print(data[0]+'\t'+str(pos)+'\t'+ref+'\t'+alt[i]+
			'\tAC:'+AC[i]+
			'\tAF:'+AF[i]+
			'\tAC_AFR:'+AC_AFR[i]+
			'\tAC_AMR:'+AC_AMR[i]+
			'\tAC_ASJ:'+AC_ASJ[i]+
			'\tAC_EAS:'+AC_EAS[i]+
			'\tAC_FIN:'+AC_FIN[i]+
			'\tAC_NFE:'+AC_NFE[i]+
			'\tAC_OTH:'+AC_OTH[i]+
			'\tAC_SAS:'+AC_SAS[i]+
			'\tAC_Male:'+AC_Male[i]+
			'\tAC_Female:'+AC_Female[i]+
			'\tAN_AFR:'+AN_AFR[0]+
			'\tAN_AMR:'+AN_AMR[0]+
			'\tAN_ASJ:'+AN_ASJ[0]+
			'\tAN_EAS:'+AN_EAS[0]+
			'\tAN_FIN:'+AN_FIN[0]+
			'\tAN_NFE:'+AN_NFE[0]+
			'\tAN_OTH:'+AN_OTH[0]+
			'\tAN_SAS:'+AN_SAS[0]+
			'\tAN_Male:'+AN_Male[0]+
			'\tAN_Female:'+AN_Female[0]+
			'\tAF_AFR:'+AF_AFR[i]+
			'\tAF_AMR:'+AF_AMR[i]+
			'\tAF_ASJ:'+AF_ASJ[i]+
			'\tAF_EAS:'+AF_EAS[i]+
			'\tAF_FIN:'+AF_FIN[i]+
			'\tAF_NFE:'+AF_NFE[i]+
			'\tAF_OTH:'+AF_OTH[i]+
			'\tAF_SAS:'+AF_SAS[i]+
			'\tAF_Male:'+AF_Male[i]+
			'\tAF_Female:'+AF_Female[i]+
			'\tHom_AFR:'+Hom_AFR[i]+
			'\tHom_AMR:'+Hom_AMR[i]+
			'\tHom_ASJ:'+Hom_ASJ[i]+
			'\tHom_EAS:'+Hom_EAS[i]+
			'\tHom_FIN:'+Hom_FIN[i]+
			'\tHom_NFE:'+Hom_NFE[i]+
			'\tHom_OTH:'+Hom_OTH[i]+
			'\tHom_SAS:'+Hom_SAS[i]+
			'\tHom_Male:'+Hom_Male[i]+
			'\tHom_Female:'+Hom_Female[i]+
			'\tHom:'+Hom[i]+
			'\tPOPMAX:'+POPMAX[i]+
			'\tAC_POPMAX:'+AC_POPMAX[i]+
			'\tAN_POPMAX:'+AN_POPMAX[i]+
			'\tAF_POPMAX:'+AF_POPMAX[i])


file = open("gnomad.exomes.r2.0.1.sites.vcf_head20000", "r")
info = file.readlines()

#print(info[300:400])

data = []
for line in info:
	if line[0]=='#':
		#print(line.strip() + '\tannotation')
		pass
	else:
		data.extend(line.split('\t'))
		if len(data) >= 8:
			print_gene(data)
			data = []