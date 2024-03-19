"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import Category_Controller
from . import Subcategory_Controller
from . import Brand_Controller
from . import Product_Controller
from . import Login_Controller
from . import Registration_Controller
from . import UserInterface
from . import web
from . import picture

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoryinterface/', Category_Controller.Category_Interface),
    path('submitcategory', Category_Controller.Submit_Category),
    path('editcategory', Category_Controller.Edit_Category),
    path('editcategoryicon', Category_Controller.Edit_CategoryIcon),
    path('deletecategory', Category_Controller.Delete_Category),
    path('displayallcategories/', Category_Controller.Display_All_Category),
    path('fetchallcategoryjson', Category_Controller.Fetch_All_Category_JSON),

    path('subcategoryinterface/', Subcategory_Controller.SubCategory_Interface),
    path('submitsubcategory', Subcategory_Controller.Submit_SubCategory),
    path('displayallsubcategories/', Subcategory_Controller.Display_All_SubCategory),
    path('editsubcategory', Subcategory_Controller.Edit_SubCategory),
    path('deletesubcategory', Subcategory_Controller.Delete_SubCategory),
    path('editsubcategoryicon', Subcategory_Controller.Edit_SubCategoryIcon),

    path('brandinterface/', Brand_Controller.Brand_Interface),
    path('submitbrand', Brand_Controller.Submit_Brand),
    path('displayallbrands/', Brand_Controller.Display_All_brand),
    path('fetchallsubcategoryjson', Brand_Controller.Fetch_All_SubCategory_JSON),
    path('editbrand', Brand_Controller.Edit_Brand),
    path('deletebrand', Brand_Controller.Delete_Brand),
    path('editbrandicon', Brand_Controller.Edit_BrandIcon),

    path('productinterface/', Product_Controller.Product_Interface),
    path('submitproduct', Product_Controller.Submit_Product),
    path('displayallproduct/', Product_Controller.Display_All_Product),
    path('fetchallbrandjson', Product_Controller.Fetch_All_Brand_JSON),
    path('fetchallproductjson', Product_Controller.Fetch_All_Product_JSON),
    path('editproduct', Product_Controller.Edit_Product),
    path('deleteproduct', Product_Controller.Delete_Product),
    path('editproducticon', Product_Controller.Edit_ProductIcon),

    path('loginpage/', Login_Controller.Login_Interface),
    path('checklogin', Login_Controller.Submit_Login),
    path('logout/', Login_Controller.Admin_Logout),

    path('registrationpage/', Registration_Controller.Regi_Interface),
    path('submitregister', Registration_Controller.Submit_Registration),

    path('home/', UserInterface.Index),
    path('fetch_all_user_category/', UserInterface.Fetch_All_Category_JSON),
    path('fetch_all_user_subcategory/', UserInterface.Fetch_All_SubCategory_JSON),

    path('fetch_all_product/', UserInterface.Fetch_All_Products),
    path('buy_product', UserInterface.Buy_Product),
    path('add_to_cart', UserInterface.AddToCart),
    path('fetch_cart/', UserInterface.FetchCart),
    path('remove_from_cart/', UserInterface.RemoveFromCart),
    path('my_shopping_cart/', UserInterface.MyShoppingCarts),
    path('check_user_mobileno/', UserInterface.CheckUserMobileno),
    path('insert_user/', UserInterface.InsertUser),
    path('check_user_mobileno_for_address/', UserInterface.CheckUserMobilenoForAddress),
    path('insert_user_address/', UserInterface.InsertUserAddress),
    path('iuser_address/', UserInterface.IUserAddress),
    path('picture/', picture.picture),
    path('submitpicture', picture.submitpicture),
    path('webpage/', web.web),
    path('fetchweb/', web.FetchWeb),

]
