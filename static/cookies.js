function uid() {
      return (performance.now().toString(36)+Math.random().toString(36)).replace(/\./g,"");
      };


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
         }
      }
      return cookieValue;
    }


var csrftoken = getCookie('csrftoken');



