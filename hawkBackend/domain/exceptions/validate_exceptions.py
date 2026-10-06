

class ValidateException(
    Exception
):
    def __init__(self ,errors : dict[str,list[str]], message : str = "There are validations errors", *args, **kwargs):
        super().__init__(message , *args)
        self.errors = errors

    def __str__(self):
        return "error in: ".join([f"{field} : {error}" for field , error in self.errors.values()])
