// func.js

function hint(key):
{
    if ((key == Qt.Key_F1))
        if (debug.visible) {
            debug.visible = false
            btn.text = "<font color='#ffffff'>" + "Hint"
        }
        else {
            debug.visible = true
            btn.text = "<font color='#000000'>" + "Hint"
        }
        counter.text = "123"
}
