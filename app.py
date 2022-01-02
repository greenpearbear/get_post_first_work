from flask import Flask, request, render_template, send_from_directory
import json
import def_tag

with open('posts.json', 'r', encoding='utf-8') as fh:
    data_json = json.load(fh)

app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template("index.html", dict=def_tag.search_tag(data_json))


@app.route("/tag/")
def page_tag():
    search = '#' + request.args.get('tag', '')
    dict_result = []
    for value in data_json:
        if search in value['content']:
            dict_result.append(value)
    return render_template("tag.html", data=dict_result, tag=search)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == "GET":
        return render_template("post.html")
    if request.method == "POST":
        picture = request.files['pic']
        picture.save(f'uploads/picture_{len(data_json)+1}.jpg')
        way = f'/uploads/picture_{len(data_json)+1}.jpg'
        content = request.form.get('content')
        new_dict = {"pic": way, 'content': content}
        data_json.append(new_dict)
        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump(data_json, f)
        return render_template('uploads.html', content=content, way=way)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(500)
def internal_error(error):
    return 'Ошибка загрузки'


app.run(debug=True)
