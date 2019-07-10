
# nested functions

def outer(db):
    def inner(dbtype):
        if dbtype == 'Document-oriented':
            return "'{0}' {1} store object's data in documents.".format(dbtype,db)
        elif dbtype == 'Relational':
            return "'{0}' {1} store data in tables.'".format(dbtype,db)
    return inner
    
doc_db = outer('databases')
print(doc_db('Document-oriented'))
rel_db = outer('databases')
print(rel_db('Relational'))
print("------------------------------")

def outer(nosql):
    def inner(feature):
        if feature == 'Fields':
            return "'{0}' in {1} document can be indexed with primary and secondary indeces.".format(feature, nosql)
        elif feature == 'Replica sets':
            return "'{0}' are available in {1}. ".format(feature,nosql)
        elif feature == 'sharding':
            return "{0} scales horizontaly using '{1}'.".format(nosql, feature)
        elif feature == 'GridFS':
            return "{0} can be used as a file system, called '{1}'.".format(nosql, feature)
        elif feature == 'aggregation':
            return "{0} provides 3 ways to perform {1}.".format(nosql, feature)
        elif feature == 'capped collections':
            return "{0} supports fixed-sized collections called '{1}'.".format(nosql, feature)
        else:
            return "Support for multi-document ''{0}' was added to {1} in 2018.".format(feature,nosql)
    return inner
    
field = outer('MongoDB')
print(field('Fields'))
sets = outer('MongoDB')
print(sets('Replica sets'))
shard = outer('MongoDB')
print(shard('sharding'))
gridfs = outer('MongoDB')
print(gridfs('GridFS'))
aggr = outer('MongoDB')
print(aggr('aggregation'))
coll = outer('MongoDB')
print(coll('capped collections'))
acid = outer('MongoDB')
print(acid('ACID'))
print("------------------------------")

def outer(feature):
    def inner(detail):
        return "'{0}' is a '{1}' of data in a database or search engine.".format(feature, detail)
    return inner
    
innerfunc = outer('Database shard') 
innerfunc('horizontal partition')
print("------------------------------")

def outer(mongo):
    def inner(feature):
        def inner2 (detail):
            return "In {0} '{1}' is a '{2}' of data in a database or search engine.".format(mongo, feature, detail)
        return inner2
    return inner

innerf = outer('MongoDB')
innerf2 = innerf('database shard')
innerf2('horizontal partition')
print("------------------------------")

def outer(doc):
    def inner(mongo):
        def inner2(feature):
            def inner3(detail):
                return "In {0}, which is a '{1}', '{2}'' is a '{3}' of data in a database or search engine.".format(mongo, doc, feature, detail)
            return inner3
        return inner2
    return inner

innerf = outer('document-oriented database')
innerf2 = innerf('MongoDB')
innerf3 = innerf2('database shard')
print(innerf3('horizontal partition'))
print("------------------------------")

def outer(nosql):
    def inner(doc):
        def inner2(mongo):
            def inner3(feature):
                def inner4(detail):
                    return "There are many {0} databases.\nIn {1}, which is a '{2}', '{3}' is a '{4}' of data in a database or search engine.".format(nosql, mongo, doc, feature, detail)
                return inner4
            return inner3
        return inner2
    return inner

innerf = outer('noSQL')
innerf2 = innerf('document-oriented database')
innerf3 = innerf2('MongoDB')
innerf4 = innerf3('database shard')
print(innerf4('horizontal partition'))
print("------------------------------")


def outer(feature):
    def inner(detail):
        return "'{0}' is a '{1}' of data in a database or search engine.".format(feature, detail)
    return inner

innerfunc = outer('Database shard') 
print(innerfunc('horizontal partition'))
outer('shard')
print("------------------------------")


def outer(feature):
    def inner(detail):
        return "'{0}' is a '{1}' of data in a database or search engine.".format(feature, detail)
    return inner('horizontal partition')

outer('Database shard')






