function toggle_div(id)
{
    a = document.getElementById(id);
    if (a.style.display == "none")
        a.style.display = "block";
    else
        a.style.display = "none";
}
function setbg(id, color)
{
    document.getElementById(id).style.background=color;
}
function addtask()
{
    name = $('#newtask').val()
    if (name=="")
    {
        alert("事务名称不能为空.");
        return;
    }
    splace = document.getElementById("task_place")
    place  = splace.options[splace.selectedIndex].text;
    sproject = document.getElementById("task_proj")
    project =  sproject.options[sproject.selectedIndex].text;
    sdeadline= document.getElementById("task_time")
    deadline =  sdeadline.options[sdeadline.selectedIndex].text;

    scolor = document.getElementById("task_color")
    color =  scolor.options[scolor.selectedIndex].text;
    if (deadline == "现在")

}
