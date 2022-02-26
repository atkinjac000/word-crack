<script>
	import { onMount } from 'svelte';

	let new_word = "";
	let guess = "";

	let good_guesses = [];
	let other_guesses = [];

	let url = "http://localhost:5000/api/";

	async function get_word() {
		let response = await fetch(url + "new_word");
		new_word = await response.json();
		good_guesses = [];
		other_guesses = [];
		guess = "";
	}

	async function check_word() {
		let response = await fetch(url + "check_word?word=" + guess);
		response = await response.json();
		if (response.data.is_word) {
			if (validate_word()) {
						if (!good_guesses.some((element) => element.word == response.data.word)){
							good_guesses = [response.data, ... good_guesses];
						}
				}
		} else {
			if (!other_guesses.some((element) => element.word == response.data.word)){
				other_guesses = [response.data, ... other_guesses];
			}
		}
		guess = "";
	}

	function validate_word() {
		let guess_array = Array.from(guess);
		guess_array = guess_array.map(char => new_word.includes(char));
		return guess_array.every(elem => elem == true);
	}

	onMount(async () => {
		get_word()
	});
</script>

<main>
	<h1>Word Crack</h1>
	<h4>Your word is: { new_word }</h4>

	<input id="guess_input" bind:value={guess} type="text"/>
	<button on:click={check_word}>Check my guess!</button>

	<h4>Good guesses:</h4>
	{#each good_guesses as user_guess}
		<p>{user_guess.word}</p>
	{/each}

	<h4>Bad guesses:</h4>
	{#each other_guesses as user_guess}
		<p>{user_guess.word}</p>
	{/each}

	<button on:click={get_word}>New Word</button>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
