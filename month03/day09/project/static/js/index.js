// 外部JS文件
$(function () {
    // 当页面元素加载完成之后执行的代码
    // console.log(blogData);
    // console.log(faderData);
    // console.log('数据加载成功');

    // 声明本地路径 路径可能变化，通常采用地址+图片名进行拼接
    var BASE_URL = '../static/images/'
    // 使用faderData在页面加载所有的轮播图
    var html = '';// 保存所有字符串
    $.each(faderData, function(i, e) {
        url = `${BASE_URL}${e.img_url}`;
        html += '<li class="slide">';
        html += '<a href="#">';
        html += `<img src=${url} alt="">`;
        html += `<span>${e.img_info}</span>`;
        html += '</a>';
        html += '</li>';
    })
    $('.fader_controls').before(html);
    console.log(html);

    // jquery-->easyfader-->index
    $('.fader').easyFader();

    // 加载页面中的博客
    // 使用JS 从blogData中加载前4个数据到页面中
    function add_blogs(data) {
        
        var html = '';
        $.each(data, function (i, e) {
            // console.log(`${e.blogtitle}`);
            // console.log(`${e.blogpic}`);
            html += `<div class="blogs">
                        <h3 class="blogtitle">
                            <a href="#">
                                ${e.blogtitle}
                            </a>
                        </h3>
                        <div class="blogpic">
                            <img src=${BASE_URL}${e.blogpic} alt="">
                        </div>
                        <p class="blogtext">
                            ${e.blogtext}
                        </p>
                        <ul>
                            <li class="author">${e.bloginfo.author}</li>
                            <li class="lname">${e.bloginfo.lmname}</li>
                            <li class="timer">${e.bloginfo.timer}</li>
                            <li class="view">${e.bloginfo.view}</li>
                            <li class="like">${e.bloginfo.like}</li>
                        </ul>
                    </div>`
        })// 循环结束
        $('.blogsbox').append(html);
    }// 函数结束

    // 加载前四条数据
    add_blogs(blogData.slice(0,4));
    // 滚动条滚动事件
    $(document).scroll(function () {
        // 当数据快要浏览完毕时添加
        // 完整文档高度
        var documentHeight = $(document).height();
        // 窗口可视范围高度
        var windowHeight = $(window).height();
        // 滚动条高度
        var scrollTop = $(document).scrollTop();
        // console.log(documentHeight, windowHeight, scrollTop);
        if (documentHeight - windowHeight - scrollTop <= 200) {
            console.log("快到底了")
            // 快到底时加载后5条数据
            // 通过查找blogs class，使用length得到页面中元素数量
            var n = $('.blogs').length;
            var data = blogData.slice(n, n + 5);
            // console.log(data);
            if (data.length > 0) {
                add_blogs(data);
            } else {
                alert("没数据啦");
            }
            
        }
    })
})
