function erase(id)
// erase the text whose id is id
{
    document.getElementById(id).value = "";
}

function check_email(id, show_id)
{
    email = document.getElementById(id)
    pattern = /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/;
    if (pattern.test(email.value))
    {
        return true;
    }
    else
    {
        if (email.value.length !=0 )
            show_div(show_id);
        return false;
    }
}
function show_div(id)
{
    document.getElementById(id).style.display = "block";
}
function hide_div(id)
{
    document.getElementById(id).style.display="none";
}
function check_length(id, length, show_id)
{
    str = document.getElementById(id).value;
    if (str.length < length)
    {
        if (str.length != 0)
            show_div(show_id);
        return false;
    }
    else
    {
        return true;
    }
}
function check_equal(id1, id2, show_id)
{
    a = document.getElementById(id1).value;
    b = document.getElementById(id2).value;
    if (a==b)
    {
        return true;
    }
    else
    {
        show_div(show_id);
        return false;
    }
}
function check_name(id, show_id)
{
    pattern = /^[a-zA-Z][\w]*$/;
    name = document.getElementById(id).value;
    if (pattern.test(name))
    {
        return true;
    }
    else
    {
        if (name.length!=0)
            show_div(show_id);
        return false;
    }
}

function check_all(id1, id2, id3, id4, show_id)
{
    a = document.getElementById(id1).value;
    b = document.getElementById(id2).value;
    c = document.getElementById(id3).value;
    d = document.getElementById(id4).value;
    error = document.getElementById(show_id);
    if (a=="")
    {
       error.innerHTML = "<font color='red' size='2px'>用户名不能为空.</font>";
       show_div(show_id);
       return false;
    }
    if (!check_name(id1, show_id))
    {
       error.innerHTML = "<font color='red' size='2px'>用户名格式不正确.</font>";
       show_div(show_id);
       return false;
    }
    if (b=="")
    {
       error.innerHTML = "<font color='red' size='2px'>email不能为空.</font>";
       show_div(show_id);
       return false;
    }
    if (!check_email(id2, show_id))
    {
       error.innerHTML = "<font color='red' size='2px'>email格式不正确.</font>";
       show_div(show_id);
       return false;
    }
    if (c=="")
    {
       error.innerHTML = "<font color='red' size='2px'>密码不能为空.</font>";
       show_div(show_id);
       return false;
    }
    if (!check_length(id3, 6, show_id))
    {
       error.innerHTML = "<font color='red' size='2px'>密码长度应大于等于6.</font>";
       show_div(show_id);
       return false;
    }
    if (d == "")
    {
       error.innerHTML = "<font color='red' size='2px'>两次密码不相同.</font>";
       show_div(show_id);
       return false;
    }
    if (!check_equal(id3, id4, show_id))
    {
       error.innerHTML = "<font color='red' size='2px'>两次密码不相同.</font>";
       show_div(show_id);
       return false;
    }

    return true;
}

function isvalid(host, id, show_id)
{
    name = $('#'+id).val()
    if (name == "")
    {
        show_div(show_id);
        return false;
    }
    $.ajax({
        url:host+"/checkname/",
        type:"POST",
        data: "username="+name,
        beforeSend: function(){
                tip = "<font color='green' size='2px'>正在查询...</font>";
                document.getElementById(show_id).innerHTML = tip;
                document.getElementById(show_id).style.display = "block";
        },

        success: function(data){
            if (data == "OK")
            {
                tip = "<font color='red' size='2px'>用户名可用</font>";
            }
            else
            {
                tip = "<font color='red' size='2px'>用户名不可用</font>";

            }
            document.getElementById(show_id).innerHTML = tip;
            document.getElementById(show_id).style.display = "block";
        },
    });
}


    
