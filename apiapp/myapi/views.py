from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random,math

@api_view(['GET'])
def getquote(request):

    r=math.trunc(random.random()*10)

    d={
        '0':'For every minute you are angry you lose sixty seconds of happiness. ― Ralph Waldo Emerson',
        '1':"I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best. ― Marilyn Monroe",
        '2':'So many books, so little time. ― Frank Zappa {}'.format(r),
        '3':"Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. ― Albert Einstein",
        '4':"Be the change that you wish to see in the world. ― Mahatma Gandhi",
        '5':"If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals. ― J.K. Rowling, Harry Potter and the Goblet of Fire",
        '6':"If you tell the truth, you don't have to remember anything. ― Mark Twain",
        '7':"To live is the rarest thing in the world. Most people exist, that is all. ― Oscar Wilde",
        '8':"A woman is like a tea bag; you never know how strong it is until it's in hot water. ― Eleanor Roosevelt",
        '9':"I have not failed. I've just found 10,000 ways that won't work. ― Thomas A. Edison"
    }

    result = {
        'Quote':d[str(r)]
    }

    return Response(result, status=status.HTTP_200_OK)