// https://kf8f3w2kg1.execute-api.us-west-2.amazonaws.com/default/handleLead

function submitLead() {
  $.ajax({
    type: 'POST',
    url: 'https://kf8f3w2kg1.execute-api.us-west-2.amazonaws.com/default/handleLead',
    data: $('#lead-form').serialize(),
    success: function(data) {
      console.log('success')
    },
    error: function(data) {
      console.log('error')
    },
  })
}
