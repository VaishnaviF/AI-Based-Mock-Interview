
import datetime

def getdate():

	today = datetime.date.today()
	formatted_date = today.strftime("%d-%m-%Y")

	return formatted_date

	
if __name__ == '__main__':
	print(main())