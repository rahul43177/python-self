from pydantic import BaseModel , Field

class Comment(BaseModel) :
    text : str = Field(min_length = 1)
    likes : int = Field(default=0)

class BlogPost(BaseModel):
    title:str = Field(min_length=1)
    comments : list[Comment]

new_comment = Comment(
    text = "It was really really good" ,
    likes = 12
)

new_comment_1 = Comment(
    text = "it was okayish i tried yest",
    likes = 20
)


new_blog = BlogPost(
    title="How to be fit" ,
    comments=[new_comment , new_comment_1]
)

data = new_blog.model_dump()
print(data)
print(new_blog)

#{'title': 'How to be fit', 'comments': [{'text': 'It was really really good', 'likes': 12}, {'text': 'it was okayish i tried yest', 'likes': 20}]}
