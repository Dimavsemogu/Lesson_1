from horoscope import *

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""
	<head><meta chatset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body(list_times, list_advices, list_promises, header):
	body = f"<h1>{header}</h1>"
	body += f"<body>{list_times}{list_advices}{list_promises}</body>"
	body += f'<a href = "%s" >Главная страница</a>' % "index.html"
	return body

def generate_list_times(times):
	list_times = "<ul>" + "<li>" + "Времена дня:" + "</li>"
	list_times += "<ol>"
	for i in times:
		list_times += f"<li>{i}</li>"
	list_times += "</ol>"
	return list_times

def generate_list_advices(advices):
	list_advices = "<li>" + "Глаголы:" + "</li>"
	list_advices += "<ol>"
	for i in advices:
		list_advices += f"<li>{i}</li>"
	list_advices += "</ol>"
	return list_advices

def generate_list_promises(promises):
	promises_1 = promises[0]
	promises_2 = promises[1]
	promises_3 = promises[2]
	promises_4 = promises[3] 
	list_promises = "<li>" + "Обещания:" + "</li>"
	list_promises += "<ol>"
	for i in promises:
		list_promises += f"<li>{i}</li>"
	list_promises += "</ol>" + "</ul>"
	return list_promises

def save_page(title,  header, output = "about.html"):
	fp = open(output, "w", encoding = "utf-8")
	page = generate_page(
		head = generate_head(title),

		body = generate_body(
			header = header,
			list_times = generate_list_times(times), 
			list_promises = generate_list_promises(promises), 
			list_advices = generate_list_advices(advices)
			), 
	)
	print(page, file = fp)
	fp.close()

##########################

save_page(
	title = "О чем все это",
	header = "О чем все это", 
	)