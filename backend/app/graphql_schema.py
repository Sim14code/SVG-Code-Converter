
import strawberry
import uuid, os
from strawberry.file_uploads import Upload
from .model_utils import image_to_svg

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@strawberry.type
class ConversionResult:
    id: str
    svg: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def upload_image(self, file: Upload) -> ConversionResult:
        file_id = str(uuid.uuid4())
        path = f"{UPLOAD_DIR}/{file_id}.png"
        with open(path, "wb") as f:
            f.write(file.read())

        svg_code = image_to_svg(path)
        return ConversionResult(id=file_id, svg=svg_code)

schema = strawberry.Schema(mutation=Mutation)
