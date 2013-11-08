import web
import json

urls = (
    '/', 'index'
)

class index:
    def GET(self):
	report_data = web.input()
        return "hello world get" + report_data.chipid
    def POST(self):
	report_data = web.input()
	this_chip_id = report_data.chipid
	print(this_chip_id)
	if this_chip_id == "23456789abcaef01":
	    resultDict = {"rnd":123456, "counter":001}
	    return json.dumps(resultDict)
        else:
	    return "no found"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
