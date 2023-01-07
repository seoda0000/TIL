const DUMMY_DATA = [
  {
    id: "m1",
    title: "This is a first meetup",
    image:
      "https://www.cabq.gov/artsculture/biopark/news/10-cool-facts-about-penguins/@@images/1a36b305-412d-405e-a38b-0947ce6709ba.jpeg",
    address: "Meetupstreet 1, 12345 Meetup City",
    description:
      "This is a first, amazing meetup which you definitely should not miss. Come and join us!",
  },
  {
    id: "m2",
    title: "This is a second meetup",
    image:
      "https://i.natgeofe.com/n/09ab5a40-53d1-4ca5-9f4c-e81011444fd1/penguins_01_3x4.jpg",
    address: "Meetupstreet 2, 12345 Meetup City",
    description:
      "This is a second, amazing meetup which you definitely should not miss. Come and join us!",
  },
];

function AllMeetupsPage() {
  return (
    <section>
      <h1>All Meetups Page</h1>
      <ul>
        {DUMMY_DATA.map((meetup) => {
          return <li key={meetup.id}>{meetup.title}</li>;
        })}
      </ul>
    </section>
  );
}

export default AllMeetupsPage;
