from django.shortcuts import redirect, render
import random

# python manage.py


def index(request):

    if 'gold_count' in request.session:
        print("Nothing")
    else:
        request.session['gold_count'] = 0

    if 'activity' in request.session:
        print("logs!")
    else:
        request.session['activity'] = []
        # request.session.save()

    return render(request, 'index.html')


# def process_farm(request):

#     # FARM earn 10 - 20 gold
#     random_gold = random.randint(10, 20)
#     request.session['gold_count'] += random_gold
#     print(request.session['gold_count']
#     # logs.append(f"{random_gold} gold added to count")

#     return redirect('/')

def process_cave(request):

    # CAVE earn 5 - 10 gold
    random_gold=random.randint(5, 10)
    request.session['gold_count'] += random_gold
    print(request.session['gold_count'])
    request.session['activity'].append(f"{random_gold} gold added to count")
    request.session.save()

    return redirect('/')

def process_house(request):

    # HOUSE earn 2 - 5 gold
    random_gold=random.randint(2, 5)
    request.session['gold_count'] += random_gold
    print(request.session['gold_count'])

    return redirect('/')

def process_casino(request):

    # CASINO Earn/Lose 0 - 50 gold
    random_gold=random.randint(-50, 50)
    print(random_gold)
    # No need to check for negatives because( 10 + -5 = 5)
    request.session['gold_count'] += random_gold
    print(request.session['gold_count'])

    return redirect('/')

def clear(request):

    request.session.clear()
    print("Session was cleared")

    return redirect('/')
