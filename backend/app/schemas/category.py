from pydentic import BaseModel, Field
#общие поля для схем
class CategoryBase(BaseModel):
    name: str = Field(... , min_length = 5, max_length = 100, description = "Category name") 
    slug: str = Field(... , min_length = 5, max_length = 100, description = "URL-friendly category name") 


class CategoryCreate(CategoryBase):
    pass
#детальная информация о категории 
class CategoryResponse(CategoryBase):
    id:  int = Field(... , description = 'Unique category identtifier')

    class Config:
        from_attributes = True #создание схемы напрямую из модели 