// https://kf8f3w2kg1.execute-api.us-west-2.amazonaws.com/default/handleLead

function submitLead() {
  var _button = $('#lead-submit')
  _button.prop('disabled', true)
  _button.attr('class', 'submitting')
  _button.val('SENDING...')

  $.ajax({
    type: 'POST',
    url: 'https://kf8f3w2kg1.execute-api.us-west-2.amazonaws.com/default/handleLead',
    data: $('#lead-form').serialize(),
    success: function() {
      $('#lead-form').find('input[type=text], input[type=email], textarea').val('')
      _button.prop('disabled', false)
      _button.attr('class', '')
      _button.val('THANKS!')
    },
    error: function() {
      _button.prop('disabled', false)
      _button.attr('class', 'error')
      _button.val('TRY AGAIN')
    },
  })
}
