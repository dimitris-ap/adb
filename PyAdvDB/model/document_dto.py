class DocumentDto(object):

    def __init__(self, filename, path, content, sample, title, *args, **kwargs):
        self.filename = filename
        self.path = path
        self.content = content
        self.sample = sample
        self.title = title

    def serialize(self):
        return {
            'path': self.path,
            'filename': self.filename,
            'content': self.content,
            'sample': self.sample,
            'title': self.title
        }
