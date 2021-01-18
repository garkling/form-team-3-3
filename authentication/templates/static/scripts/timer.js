document.addEventListener('DOMContentLoaded', function() {
	const date = document.getElementById('timer')

	const orderEnd = new Date(+date.dataset.date).getTime()

	const x = setInterval(function () {

		const now = new Date().getTime();
		const distance = orderEnd - now;

		const days = Math.floor(distance / (1000 * 60 * 60 * 24));
		const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		const seconds = Math.floor((distance % (1000 * 60)) / 1000);

		document.getElementById("timer").innerHTML = `${days} : ${hours} : ${minutes} : ${seconds}`;

		if (distance < 0) {
			clearInterval(x);
			document.getElementById("timer").innerHTML = "Expired";
		}
	}, 1000);
})
