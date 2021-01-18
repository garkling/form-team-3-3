document.addEventListener('DOMContentLoaded', function () {
	const submitButton = document.getElementById('submit-order-btn')
	const returnButton = document.getElementById('return-book-btn')
	const options = {
		html: 'Success!!',
		classes: 'rounded'
	}

	submitButton.addEventListener('click', () => M.toast(options) )
	returnButton.addEventListener('click', () => M.toast(options) )
})
