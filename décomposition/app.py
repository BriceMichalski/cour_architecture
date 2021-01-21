from flask import Flask
from flask import request

from validator import is_present,is_valid,is_spam

app = Flask(__name__)
spam_list = ['spamming.com', 'mailinator.com', 'oneminutemail.com']

@app.route('/')
def mail_validation():
    email = request.args.get('email')
    conditions = [
        {"function": is_present , "expected": True, "args":[email]},
        {"function": is_valid , "expected": True, "args":[email]},
        {"function": is_spam , "expected": False, "args":[email,spam_list]}
    ]

    for cond in conditions:
        result,msg = check_condition(cond['function'],cond['expected'],*cond['args'])
        if result is not True:
            return msg

    return 'is Valid'

def check_condition(func,expected,*args):
    try:
        satisfy = func(*args) is expected
        if satisfy:
            message = None
        else:
            message = "email {}".format(
                func.__name__.replace("_"," " if satisfy == expected == False else " not ")
            )
        return satisfy,message
    except Exception as e:
        print(e)
        return None, "{} \n ".format(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)

