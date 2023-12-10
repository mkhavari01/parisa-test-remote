from django.http import JsonResponse
from api.recommendation import content_based_recom



def suggest_food(request):
    user_id = request.GET.get('user_id', '1')
    user_title = request.GET.get('user_title', 'title')
    print("user id is",user_title)
    recommendations = content_based_recom(user_id)
    return JsonResponse({'recommendations': recommendations,"user_title" : user_title})
    # return JsonResponse({
    #     "test" : "1234"
    # })
    # elif request.method == 'POST':
    #     user_id = request.POST.get('user_id')
    #     recommendations = content_based_recom(user_id)
    #     return JsonResponse({'recommendations': recommendations})



