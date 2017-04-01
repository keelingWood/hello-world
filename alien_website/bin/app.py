import web

urls = (
    '/hello','Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")
print('running')

class Index(object):
    def GET(self):
        print('get')
        return render.hello_form()
    
    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        print('post')
        return render.index(greeting = greeting)
        
if __name__ == "__main__":
    app.run()