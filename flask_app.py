from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("/index.html")

@app.route('/shortq', methods = ['POST', 'GET'])
def shortq():
    return render_template("/shortq.html")

@app.route('/basicq', methods = ['POST','GET'])
def basicq():
    return render_template("/basicq.html")

@app.route('/questionnaire', methods = ['POST','GET'])
def questionnaire():
    return render_template("/questionnaire.html")

@app.route('/fullq', methods = ['POST','GET'])
def fullq():
    return render_template("/fullq.html")

@app.route('/homepageTEST')
def homepageTEST():
    return render_template("homepageTEST.html")

@app.route('/temp')
def temp():
    return render_template("temp.html")

@app.route('/about')
def about():
    return render_template("/about.html")

@app.route('/product_pg', methods = ['POST','GET'])
def product_pg():
    if request.method == 'POST':

        prodnum=[]
        name=[]
        price=[]
        desc=[]
        img=[]

        gender = request.form['gender']

        if gender == "IDK!": # RANDOM option
            with sqlite3.connect('GiftFinder.db') as conn:
                curs = conn.cursor()
                sql = ("""SELECT product_no, product_name, product_price, product_desc, product_img FROM tblProducts ORDER BY RANDOM();""")
                for row in curs.execute(sql):
                        product_no,product_name,product_price,product_desc,product_img = row
                        prodnum.append(product_no)
                        name.append(product_name)
                        price.append(product_price)
                        desc.append(product_desc)
                        img.append(product_img)

            conn.close()
            return render_template('product_pg.html', product_no=prodnum, name=name, price=price, desc=desc, img=img, length = len(name))

        else:
            # basic refine options
            btags= []

            if gender == "othergen": # if they select other gender, both male and female products will come up
                pass
            else:
                btags.append(gender)

            age = request.form['age']
            btags.append(age)

            priceRange = request.form['priceRange']
            if priceRange == "anyprice": # if they select no budget, any product with any price will show up
                pass
            else:
                btags.append(priceRange)

            specEvent = request.form['specEvent']
            if specEvent == "evnone":
                pass # if they pick no event, any product with any event will show up
            else:
                btags.append(specEvent)

            # specific categories
            tags= []

            clothing = request.form.getlist('clothing[]')
            if len(clothing) != 0:
                #tags.append('clothing')
                for tag in clothing:
                    tags.append(tag)

            makeup = request.form.getlist('makeup[]')
            if len(makeup) != 0:
                #tags.append('makeup')
                for tag in makeup:
                    tags.append(tag)

            skincare = request.form.getlist('skincare[]')
            if len(skincare) != 0:
                #tags.append('skincare')
                for tag in skincare:
                    tags.append(tag)

            jewelry = request.form.getlist('jewelry[]')
            if len(jewelry) != 0:
                #tags.append('jewelry')
                for tag in jewelry:
                    tags.append(tag)

            reading = request.form.getlist('reading[]')
            if len(reading) != 0:
                #tags.append('reading')
                for tag in reading:
                    tags.append(tag)

            games = request.form.getlist('games[]')
            if len(games) != 0:
                #tags.append('games')
                for tag in games:
                    tags.append(tag)

            tech = request.form.getlist('tech[]')
            if len(tech) != 0:
                #tags.append('tech')
                for tag in tech:
                    tags.append(tag)

            deco = request.form.getlist('deco[]')
            if len(deco) != 0:
                #tags.append('deco')
                for tag in deco:
                    tags.append(tag)

            quirky = request.form.getlist('quirky[]')
            if len(quirky) != 0:
                #tags.append('quirky')
                for tag in quirky:
                    tags.append(tag)

            health = request.form.getlist('health[]')
            if len(health) != 0:
                #tags.append('health')
                for tag in health:
                    tags.append(tag)

            giftcard = request.form.getlist('giftcard[]')
            if len(giftcard) != 0:
                tags.append('giftcard')

            prodnum=[]
            name=[]
            price=[]
            desc=[]
            img=[]

            btagsnum=[]

            # finds tag_no of basic tags
            with sqlite3.connect('GiftFinder.db') as conn:
                    curs = conn.cursor()
                    for btag in btags:
                        val = "'"+btag+"'"
                        sqltag = """SELECT tag_no from tblTags where tag_name ="""
                        for row in curs.execute(sqltag+val):
                            tag_no = row
                            tag_no = str(row[0])
                            btagsnum.append(tag_no)

            products= []

            # finds product_no of main tags
            for tag in tags:
                val = "'"+tag+"'"
                sqltag = """SELECT tag_no from tblTags where tag_name ="""
                for row in curs.execute(sqltag+val):
                    tag_no = str(row[0])
                    sqlprod = """SELECT tblProducts.product_no FROM tblProducts INNER JOIN tblProductTags ON tblProducts.product_no = tblProductTags.product_no where tag_No ="""
                    val2="'"+tag_no+"'"
                    # find all the products which have the tag number
                    for row in curs.execute(sqlprod+val2):
                        product_no= int(row[0])
                        if product_no not in products:
                            products.append(product_no) # consists of all products with main tags

            producttags=[]
            finalproducts=[]

            # finds tags of each product
            for product in products:
                sql= """SELECT tag_no FROM tblProductTags WHERE product_no=?"""
                for row in curs.execute(sql, (product,)):
                    tag_no = row
                    #tag_no = curs.fetchall()
                    tag_no = str(row[0])
                    producttags.append(tag_no) # consists of tags_no's of the specific product
                result =  all(elem in producttags for elem in btagsnum) # check if the product has the basic tags
                if result: # if it does, add it to the final list of products
                    finalproducts.append(product)

                    # finds tags of each product
            for product in products:
                producttags=[]
                sql= """SELECT tag_no FROM tblProductTags WHERE product_no=?"""
                for tag in curs.execute(sql, (product,)):
                    tag_no = str(row[0])
                    producttags.append(tag_no) # consists of tags_no's of the specific product
                result= set(btagsnum).issubset(producttags)
                #result =  all(elem in producttags for elem in btagsnum) # check if the product has the basic tags
                if result == True: # if it does, add it to the final list of products
                    finalproducts.append(product)


            # find data on each product
            for num in finalproducts:
                sqlprod = ("""SELECT product_no,product_name,product_price,product_desc,product_img FROM tblProducts WHERE product_no=? """)
                for row in curs.execute(sqlprod, (num,)):
                    product_no,product_name,product_price,product_desc,product_img = row # assign names to each row
                    prodnum.append(product_no) # append each product detail to a list
                    name.append(product_name)
                    price.append(product_price)
                    desc.append(product_desc)
                    img.append(product_img)

            conn.close()
            return render_template('results.html', product_no=prodnum, name=name, price=price, desc=desc, img=img, length = len(name))


@app.route('/results', methods = ['POST','GET'])
def results():
    if request.method == 'POST':

        tags= []

        prodnum=[]
        name=[]
        price=[]
        desc=[]
        img=[]

        gender = request.form['gender']

        if gender == "IDK!": # RANDOM option
            with sqlite3.connect('GiftFinder.db') as conn:
                curs = conn.cursor()
                sql = ("""SELECT product_no, product_name, product_price, product_desc, product_img FROM tblProducts ORDER BY RANDOM();""")
                for row in curs.execute(sql):
                        product_no,product_name,product_price,product_desc,product_img = row
                        prodnum.append(product_no)
                        name.append(product_name)
                        price.append(product_price)
                        desc.append(product_desc)
                        img.append(product_img)

            conn.close()
            return render_template('product_pg.html', product_no=prodnum, name=name, price=price, desc=desc, img=img, length = len(name))

        else: # Questionnaire Option

            tags.append(gender)

            age = request.form['age']
            if age != "None":
                tags.append(age)

            priceRange = request.form['priceRange']
            if priceRange != "None":
                tags.append(priceRange)

            specEvent = request.form['specEvent']
            if specEvent != "None":
                tags.append(specEvent)

            # specific categories

            clothing = request.form.getlist('clothing[]')
            if len(clothing) != 0:
                tags.append('clothing')
                for tag in clothing:
                    tags.append(tag)

            makeup = request.form.getlist('makeup[]')
            if len(makeup) != 0:
                tags.append('makeup')
                for tag in makeup:
                    tags.append(tag)

            skincare = request.form.getlist('skincare[]')
            if len(skincare) != 0:
                tags.append('skincare')
                for tag in skincare:
                    tags.append(tag)

            jewelry = request.form.getlist('jewelry[]')
            if len(jewelry) != 0:
                tags.append('jewelry')
                for tag in jewelry:
                    tags.append(tag)

            reading = request.form.getlist('reading[]')
            if len(reading) != 0:
                tags.append('reading')
                for tag in reading:
                    tags.append(tag)

            games = request.form.getlist('games[]')
            if len(games) != 0:
                tags.append('games')
                for tag in games:
                    tags.append(tag)

            tech = request.form.getlist('tech[]')
            if len(tech) != 0:
                tags.append('tech')
                for tag in tech:
                    tags.append(tag)

            deco = request.form.getlist('deco[]')
            if len(deco) != 0:
                tags.append('deco')
                for tag in deco:
                    tags.append(tag)

            quirky = request.form.getlist('quirky[]')
            if len(quirky) != 0:
                tags.append('quirky')
                for tag in quirky:
                    tags.append(tag)

            health = request.form.getlist('health[]')
            if len(health) != 0:
                tags.append('health')
                for tag in health:
                    tags.append(tag)

            giftcard = request.form.getlist('giftcard[]')
            if len(giftcard) != 0:
                tags.append('giftcard')

            with sqlite3.connect('GiftFinder.db') as conn:
                curs = conn.cursor()
                for tag in tags:
                    # put the tag into quotation marks, than concatenate it with the sql statement
                    val = "'"+tag+"'"
                    sqltag = ("""SELECT tag_no from tblTags where tag_name = """)
                    # find the tag number for the tag
                    for row in curs.execute(sqltag+val):
                        tag_no = str(row[0])
                        #print(row)
                        sqlprod = ("""SELECT tblProducts.product_no,tblProducts.product_name,tblProducts.product_price,tblProducts.product_desc,tblProducts.product_img FROM tblProducts
                        Inner JOIN tblProductTags ON tblProducts.product_no = tblProductTags.product_no where tag_No = """)
                        val2="'"+tag_no+"'"
                        # find all the products which have the tag number
                        for row in curs.execute(sqlprod+val2):
                            product_no,product_name,product_price,product_desc,product_img = row
                            if product_name not in name:
                                prodnum.append(product_no)
                                name.append(product_name)
                                price.append(product_price)
                                desc.append(product_desc)
                                img.append(product_img)

            conn.close()
            return render_template('product_pg.html', product_no=prodnum, name=name, price=price, desc=desc, img=img, length = len(name))

@app.route('/product_listing', methods=['GET'])
def product_listing():
    if request.method == 'GET':
        prodnum = request.args.get('product_no') # requests the product_no as a unique url code

    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            sql = """SELECT product_name, product_price, product_desc, product_img, product_url, company_no FROM tblProducts WHERE product_no= (?)""" # fetch the product data of the product clicked on
            for row in curs.execute(sql,(prodnum,)):
                product_name,product_price,product_desc,product_img,product_url,company_no = row

            sql2= """SELECT company_name FROM tblCompany WHERE company_no= ?"""
            curs.execute(sql2, (company_no,))
            company_name = curs.fetchall()
            company_name = company_name[0][0]

    conn.close()
    return render_template('product_listing.html', name=product_name, price=product_price, desc=product_desc, img=product_img, url=product_url, company_name=company_name)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('menu'))

    return render_template('login.html', error=error)


@app.route('/dbMenu')
def menu():
    return render_template("/dbMenu.html")

@app.route('/addprod', methods = ['POST','GET'])
def addProduct():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            company_no= []
            company_name= []
            sql = """SELECT * FROM tblCompany"""
            for row in curs.execute(sql):
                number, name = row
                company_no.append(number)
                company_name.append(name)

            tag_no= []
            tag_name= []
            sql = """SELECT * FROM tblTags"""
            for row in curs.execute(sql):
                number, name = row
                tag_no.append(number)
                tag_name.append(name)


    conn.close()
    return render_template("addprod.html", company_no=company_no, company_name=company_name, length1=len(company_no), tag_no=tag_no, tag_name=tag_name, length2=len(tag_name))


@app.route('/addresults', methods = ['POST', 'GET'])
def addresults():
    if request.method == 'POST':
        with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()

            product_name = request.form['product_name']
            product_desc = request.form['product_desc']
            product_price = request.form['product_price']
            product_url = request.form['product_url']
            product_img = request.form['product_img']
            company_no = request.form['company_no']
            # sql query to find the maximum product number
            sql = """SELECT MAX(product_no) FROM tblProducts"""
            # assign the maximum product_no from the sql to the variable maxNum
            for row in curs.execute(sql):
                maxNum = row[0]
                maxNum = maxNum+1

            val = [] # creates empty list

            # appending the list with all the values
            val.append(maxNum)
            val.append(product_name)
            val.append(product_price)
            val.append(product_desc)
            val.append(product_url)
            val.append(product_img)
            val.append(int(company_no))

            sql = """INSERT into tblProducts VALUES(?,?,?,?,?,?,?)""" # sql query
            curs.execute(sql,val) # execute the sql with the values in val
            # To save the changes in the files
            conn.commit()

        msg = "Successful"
        return render_template("addresults.html", msg=msg)
        conn.close()
    else:
        msg = "Unsuccessful"
        return render_template("addresults.html", msg=msg)


@app.route('/amendprod', methods = ['POST','GET'])
def amendprod():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            product_no= []
            product_name= []
            sql = ("SELECT product_no, product_name FROM tblProducts")
            for row in curs.execute(sql):
                number, name = row
                product_no.append(number)
                product_name.append(name)

    conn.close()
    return render_template("amendprod.html", product_no=product_no, product_name=product_name, length=len(product_name))

@app.route('/amendresults', methods = ['POST', 'GET'])
def amendresults():
    if request.method == 'POST':
        with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()

            product_no = request.form['product']
            inp = request.form['inp']
            newVal = request.form['newVal']

            val = []
            val.append(newVal)
            val.append(int(product_no))

            if inp == "name": # name
                sql = """UPDATE tblProducts SET product_name = ? WHERE product_no = ?"""
                curs.execute(sql,val)

            if inp == "desc": # desc
                sql = """UPDATE tblProducts SET product_desc = ? WHERE product_no = ?"""
                curs.execute(sql,val)

            if inp == "price": # price
                sql = """UPDATE tblProducts SET product_price = ? WHERE product_no = ?"""
                curs.execute(sql,val)

            if inp == "url": # url
                sql = ("UPDATE tblProducts SET product_url = ? WHERE product_no = ?")
                curs.execute(sql,val)

            if inp == "img": # image
                sql = """UPDATE tblProducts SET product_img = ? WHERE product_no = ?"""
                curs.execute(sql,val)

            if inp == "company_no": # image
                sql = """UPDATE tblProducts SET company_no = ? WHERE product_no = ?"""
                curs.execute(sql,val)

            conn.commit()
        conn.close()

        msg = "Successful"
        return render_template("amendresults.html", msg=msg)
        conn.close()
    else:
        msg = "Unsuccessful"
        return render_template("amendresults.html", msg=msg)

@app.route('/addcomp', methods = ['POST','GET'])
def addcomp():
    return render_template("addcomp.html")

@app.route('/addcompresults', methods = ['POST', 'GET'])
def addcompresults():
    if request.method == 'POST':
        with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()

            company_name = request.form['company_name']

            val = []
            sql = ("SELECT MAX(company_no) FROM tblCompany")
            for row in curs.execute(sql):
                maxNum = row[0]
                maxNum = maxNum+1
            val.append(maxNum)
            val.append(company_name)
            sql = ("INSERT into tblCompany (company_no, company_name) VALUES (?,?)")
            curs.execute(sql, val)
            # To save the changes in the files

            conn.commit()
        conn.close()

        msg = "Successful"
        return render_template("addcompresults.html", msg=msg)
        conn.close()
    else:
        msg = "Unsuccessful"
        return render_template("addcompresults.html", msg=msg)

@app.route('/delcomp', methods = ['POST','GET'])
def delcomp():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            company_no= []
            company_name= []
            sql = """SELECT * FROM tblCompany"""
            for row in curs.execute(sql):
                number, name = row
                company_no.append(number)
                company_name.append(name)

    return render_template("delcomp.html", company_no=company_no, company_name=company_name, length=len(company_no))
    conn.close()

@app.route('/delcompresults', methods = ['POST', 'GET'])
def delcompresults():
    if request.method == 'POST':
        with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()

            num = request.form['company_no']

            val=[]
            val.append(int(num))
            # sql query for the deletion of the record
            sql = ("DELETE FROM tblCompany WHERE company_no = (?)")
            curs.execute(sql,val)
            conn.commit()

        conn.close()
        msg = "Successful"
        return render_template("delcompresults.html", msg=msg)
    else:
        msg = "Unsuccessful"
        return render_template("delcompresults.html", msg=msg)

    conn.close()

@app.route('/delprod', methods = ['POST','GET'])
def delprod():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            product_no= []
            product_name= []
            sql = ("SELECT product_no, product_name FROM tblProducts")
            for row in curs.execute(sql):
                number, name = row
                product_no.append(number)
                product_name.append(name)

    return render_template("delprod.html", product_no=product_no, product_name=product_name, length=len(product_name))
    conn.close()

@app.route('/delresults', methods = ['POST', 'GET'])
def delresults():
    if request.method == 'POST':
        with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()

            product_no = request.form['product']

            #val = []
            # append the list with the product_no
            #val.append(int(product_no))
            # sql query for the deletion of the record
            sql = ("DELETE FROM tblProducts WHERE product_no = ?")
            curs.execute(sql, (product_no,))
            conn.commit()

        conn.close()
        msg = "Successful"
        return render_template("delresults.html", msg=msg)
    else:
        conn.close()
        msg = "Unsuccessful"
        return render_template("delresults.html", msg=msg)

@app.route('/addtag', methods = ['POST','GET'])
def addtag():
    return render_template('addtag.html')

@app.route('/addtagresults', methods = ['POST','GET'])
def addtagresults():
    if request.method == 'POST':
        with sqlite3.connect('GiftFinder.db') as conn:
                curs = conn.cursor()

                sql = """SELECT MAX(tag_no) FROM tblTags"""
                # assign the maximum tag_no from the sql to the variable maxNum
                for row in curs.execute(sql):
                    maxNum = row[0]
                    maxNum = maxNum+1

                val=[]
                name = request.form['tag_name']
                val.append(int(maxNum))
                val.append(name)

                sql = ("INSERT INTO tblTags(tag_no, tag_name) VALUES(?,?)")
                curs.execute(sql, val)
                conn.commit()

        conn.close()
        msg = "Successful"
        return render_template("addtagresults.html", msg=msg)
    else:
        conn.close()
        msg = "Unsuccessful"
        return render_template("addtagresults.html", msg=msg)


@app.route('/addprodtag', methods = ['POST','GET'])
def addprodtag():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            product_no= [] # initialise list for product numbers
            product_name= [] # initialise list for product names
            # sql query to select product numbers and names from the Database
            sql = ("SELECT product_no, product_name FROM tblProducts")
            for row in curs.execute(sql):
                number, name = row
                product_no.append(number) # adds the product number to the list
                product_name.append(name) # adds the product name to the list

            tag_no= [] # initialise list for tag numbers
            tag_name= [] # initialise list for tag names
            # sql query to select all tags from the Database
            sql2 = ("SELECT * FROM tblTags")
            for row in curs.execute(sql2):
                number1, name1 = row
                tag_no.append(number) # adds the tag number to the list
                tag_name.append(name) # adds the tag name to the list

    conn.close()
    return render_template("addprodtag.html", product_no=product_no, product_name=product_name, length=len(product_name), tag_no=tag_no, tag_name=tag_name, length2=len(tag_name))


@app.route('/productTags', methods = ['GET'])
def productTags():
    product_no = request.args.get('product_no')
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            tag_no= []
            tag_name= []
            sql1= ("SELECT tag_no, tag_name FROM tblTags")
            for row in curs.execute(sql1):
                num1, tag= row
                tag_no.append(num1)
                tag_name.append(tag)

            ptag_no=[]
            ptag_name=[]
            sql2 = ("SELECT t.tag_no, t.tag_name FROM tblTags t LEFT JOIN tblProductTags p ON p.tag_no = t.tag_no WHERE p.product_no = ?")
            for row in curs.execute(sql2, (product_no,)):
                num2, name = row
                ptag_no.append(num2)
                ptag_name.append(name)


    template = render_template("productTags.xml", tag_no=tag_no, tag_name=tag_name, tlength=len(tag_name), ptag_no=ptag_no, ptag_name=ptag_name, ptlength=len(ptag_name))

    response = make_response(template)                                 # added so that I could add XML support.
    response.headers['Content-Type'] = 'application/xml'               # I imported "make_response" at the start of the document/
    return response                                                    # replaced "ProductTags.html" with "ProductTags.xml" so ajax can read it.
    conn.close()

@app.route('/prodtagresults', methods = ['POST', 'GET'])
def prodtagresults():
    if request.method == 'POST':
        with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()

            newtags = [] # all input
            newtags = request.form.getlist('newtags')
            product_no = request.form['product']

            ptags=[] # list of tags already in product
            tempList=[] # temporary list for sql results

            sql1 = ("SELECT tag_no FROM tblProductTags WHERE product_no=(?)")
            for row in curs.execute(sql1, (product_no, )):
                num= row
                tempList.append(num)

            ptags= [str(i[0]) for i in tempList] # remove "(,)" from the sql results and turn them into strings.

            for tag in newtags: # checks to add tags
                if tag not in ptags:
                    val=[]
                    val.append(int(product_no))
                    val.append(int(tag))
                    sql2 = ("INSERT INTO tblProductTags(product_no, tag_no) VALUES (?,?)")
                    curs.execute(sql2, val)
                    conn.commit()

            for tag in ptags: # checks to delete tags
                if tag not in newtags:
                    val=[]
                    val.append(int(product_no))
                    val.append(int(tag))
                    sql3 = ("DELETE FROM tblProductTags WHERE product_no=? AND tag_no=?")
                    curs.execute(sql3, val)
                    conn.commit()

        msg = "Successful"
        conn.close()
        return render_template("prodtagresults.html", msg=msg, newtags=newtags, ptags=ptags)

    else:
        msg = "Unsuccessful"
        conn.close()
        return render_template("prodtagresults.html", msg=msg)


@app.route('/list')
def list():
    return render_template("/list.html")

@app.route('/listTags')
def listTags():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            sql = """SELECT * FROM tblTags ORDER BY tag_no DESC"""
            results = curs.execute(sql)
            return render_template("/listTags.html", rows=results)
            conn.close()

@app.route('/listProds')
def listProds():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            sql = """SELECT * FROM tblProducts ORDER BY product_no DESC"""
            results = curs.execute(sql)
            return render_template("/listProds.html", rows=results)
            conn.close()

@app.route('/listComps')
def listComps():
    with sqlite3.connect('GiftFinder.db') as conn:
            curs = conn.cursor()
            sql = """SELECT * FROM tblCompany ORDER BY company_no DESC"""
            results = curs.execute(sql)
            return render_template("/listComps.html", rows=results)
            conn.close()