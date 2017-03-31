clap_str = raw_input("Give me integer\n")
clap_int = int(clap_str)

if type(int(clap_int)) != type(0):
	print "Please enter an integer"
else:
	common_str = " clap!"
	for cnt in range(clap_int+1):
		str_cnt = str(cnt)
		if len(str_cnt) != 1:
			if str_cnt[-2] == '1':
				print str_cnt + 'th'+ common_str
			else:
				if str_cnt[-1] == '1':
					print str_cnt + 'st' + common_str
				elif str_cnt[-1] == '2':		
					print str_cnt + 'nd' + common_str
				elif str_cnt[-1] == '3':
					print str_cnt + 'rd' + common_str
				else:
					print str_cnt + 'th' + common_str
		else:
			if str_cnt[-1] == '1':
                                print str_cnt + 'st' + common_str
                        elif str_cnt[-1] == '2':
                                print str_cnt + 'nd' + common_str
                        elif str_cnt[-1] == '3':
                                print str_cnt + 'rd' + common_str
                	else:
                		print str_cnt + 'th' + common_str














