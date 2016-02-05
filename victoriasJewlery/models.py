import base64

from django.db import models

# Create your models here.
class StoreInfo(models.Model):
    storeId = models.CharField(max_length=255)
    storeUrl = models.URLField(max_length=200)
    storeName = models.CharField(max_length=255)
    invoiceLogoUrl = models.URLField(max_length=200)
    emailLogoUrl = models.URLField(max_length=200)
    starterSiteEcwidSubdomain = models.CharField(max_length=255)
    starterSiteGeneratedUrl = models.URLField(max_length=200)
    accountName = models.CharField(max_length=255)
    accountNickName = models.CharField(max_length=255)
    accountEmail = models.EmailField(max_length=254)
    customerNotificationEmail = models.EmailField(max_length=254)
    companyName = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    countryCode = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    stateOrProvinceCode = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    weightUnits = models.CharField(max_length=50)
    handlingFee = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2)

class AdminNotificationEmail(models.Model):
    storeInfo = models.ForeignKey(StoreInfo, on_delete=models.CASCADE)
    emailAddress = models.EmailField(max_length=254)

class Product(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    sku = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unlimited = models.BooleanField()
    inStock = models.BooleanField()
    name = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    priceInProductList = models.DecimalField(max_digits=20, decimal_places=2)
    compareToPrice = models.DecimalField(max_digits=20, decimal_places=2)
    isShippingRequired = models.BooleanField()
    weight = models.DecimalField(max_digits=20, decimal_places=5)
    url = models.URLField(max_length=200)
    createTimestamp = models.CharField(max_length=200)
    updateTimestamp = models.CharField(max_length=200)
    productClassId = models.IntegerField()
    enabled = models.BooleanField()
    warningLimit = models.IntegerField()
    fixedShippingRateOnly = models.BooleanField()
    fixedShippingRate = models.DecimalField(max_digits=20, decimal_places=2)
    defaultCombinationId = models.IntegerField()
    thumbnailUrl = models.URLField(max_length=200)
    imageUrl = models.URLField(max_length=200)
    smallThumbnailUrl = models.URLField(max_length=200)
    originalImageUrl = models.URLField(max_length=200)
    _description = models.TextField(
            db_column='description',
            blank=True)

    def set_data(self, description):
        self._description = base64.encodestring(description)

    def get_data(self):
        return base64.decodestring(self._description)

    description = property(get_data, set_data)
    defaultCategoryId = models.IntegerField()


class ProductWholesalePricesArray(models.Model):
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

class ProductOption(models.Model):
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)

class ProductOptionChoice(models.Model):
    parentProductOption = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    priceModifier = models.DecimalField(max_digits=20, decimal_places=2)
    priceModifierType = models.CharField(max_length=40)

class ProductGalleryImage(models.Model):
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    id = models.IntegerField(unique=True, primary_key=True)
    alt = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    thumbnail = models.URLField(max_length=200)
    width = models.IntegerField()
    height = models.IntegerField()
    imageUrl = models.URLField(max_length=200)
    orderBy = models.IntegerField()

class ProductCategoryId(models.Model):
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    categoryId = models.IntegerField()

class ProductFavoriteStat(models.Model):
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    displayCount = models.CharField(max_length=30)

class ProductAttribute(models.Model):
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    show = models.CharField(max_length=255)

class ProductFile(models.Model):
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    _description = models.TextField(
            db_column='description',
            blank=True)

    def set_data(self, description):
        self._description = base64.encodestring(description)

    def get_data(self):
        return base64.decodestring(self._description)

    size = models.IntegerField()
    adminUrl = models.URLField()

class RelatedCategory(models.Model):
    enabled = models.BooleanField()
    categoryId = models.IntegerField()
    productCount = models.IntegerField()

class ProductRelatedProducts(models.Model):
    relatedCategoryId = models.ForeignKey(RelatedCategory, on_delete=models.CASCADE)
    productId = models.IntegerField()

class Combination(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    combinationNumber = models.IntegerField()
    sku = models.CharField(max_length=255)
    smallThumbnailUrl = models.URLField(max_length=200)
    thumbnailUrl = models.URLField(max_length=200)
    imageUrl = models.URLField(max_length=200)
    originalImageUrl = models.URLField(max_length=200)
    quantity = models.IntegerField()
    unlimited = models.BooleanField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    weight = models.DecimalField(max_digits=20, decimal_places=4)
    warningLimit = models.IntegerField()

class ProductCombinationWholesalePricesArray(models.Model):
    parentProductCombination = models.ForeignKey(Combination, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)


class ProductCombinationOptionValue(models.Model):
    parentCombination = models.ForeignKey(Combination, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    defaultChoice = models.IntegerField()
    required = models.BooleanField()

class Category(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    parentId = models.IntegerField()
    orderBy = models.IntegerField()
    thumbnailUrl = models.URLField(max_length=200)
    originalImageUrl = models.URLField(max_length=200)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    productCount = models.IntegerField()
    _description = models.TextField(
            db_column='description',
            blank=True)

    def set_data(self, description):
        self._description = base64.encodestring(description)

    def get_data(self):
        return base64.decodestring(self._description)

    enabled = models.BooleanField()

class ProductType(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    googleTaxonomy = models.CharField(max_length=255)

class ProductTypeAttribute(models.Model):
    parentProductType = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=200)
    show = models.CharField(max_length=255)



