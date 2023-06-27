from core.models import Categories,SubCategories,About


def categories_context():
    contact_information = About.objects.filter(state=True).last()
    categories = Categories.objects.all()
    sub_categories = SubCategories.objects.all()
    context = {'categories': categories,'subcategories':sub_categories,'contact_information':contact_information}
    return context