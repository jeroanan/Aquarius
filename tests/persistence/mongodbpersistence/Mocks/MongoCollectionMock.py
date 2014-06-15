from pymongo.collection import Collection


class MongoCollectionMock(Collection):

    def __init__(self, database, name, **kwargs):
        self.__find_params = []
        self.__last_id = 0

    def find(self, *args, **kwargs):
        self.__find_params.append(args)
        ret_doc = self.__populate_dict_from_args(*args)
        ret_doc["_id"] = str(self.__get_id())
        return ret_doc

    def __get_id(self):
        self.__last_id += 1
        return self.__last_id

    def __populate_dict_from_args(self, *args):
        ret_doc = {}
        for k in args[0].keys():
            ret_doc[k] = args[0].get(k)
        return ret_doc

    def was_find_called_with_arg(self, arg):
        return self.__find_params.index((arg,)) > -1
