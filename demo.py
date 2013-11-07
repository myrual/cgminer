import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
	report_data = web.input()
        return "hello world get" + report_data.chipid
    def POST(self):
	report_data = web.input()
        return "hello world post" + report_data.chipid

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
