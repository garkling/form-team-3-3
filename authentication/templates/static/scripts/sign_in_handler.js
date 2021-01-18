document.addEventListener('DOMContentLoaded', function () {
	const registerFields = document.getElementById('register-fields')
	const loginButton = document.getElementById('login-btn')
	const registerButton = document.getElementById('register-btn')
	const mainForm = document.getElementById('author-form')

	loginButton.addEventListener('click', function () {
		registerFields.hidden = true
		this.type = 'submit'
		this.classList.remove('flat-btn')
		mainForm.action = "{% url 'log-in' %}"
		registerButton.type = 'button'
		registerButton.classList.add('btn-flat')
	})

	registerButton.addEventListener('click', function () {
		registerFields.hidden = false
		this.type = 'submit'
		this.classList.remove('btn-flat')
		mainForm.action = "{% url 'sign-in' %}"
		loginButton.type = 'button'
		loginButton.classList.add('btn-flat')
	});
});
