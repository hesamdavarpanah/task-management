class TwoSum:
    def __init__(self, input_list: list, target_number: int):
        self.input_list = input_list
        self.target_number = target_number
        self.result = {}

    @property
    def summary(self) -> dict:
        try:
            for i, n in enumerate(self.input_list):
                complement = self.target_number - n
                if complement in self.input_list:
                    self.result[i] = n
            return self.result
        except AttributeError as attribute_error:
            self.result['attribute_error'] = attribute_error.__str__()
            return self.result
        except KeyError as key_error:
            self.result['key_error'] = key_error.__str__()
            return self.result
        except ValueError as value_error:
            self.result['value_error'] = value_error.__str__()
        except Exception as exception:
            self.result['exception_error'] = exception.__str__()
        finally:
            return self.result
