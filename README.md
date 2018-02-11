# PyTemplate

The goal of this repository is to serve as a template for python development
with a few different real-world uses. The essence of this project is to enable
focusing on solving specific business logic related problems instead of the
scaffolding that is often required in:

- Green field work
- Interviews
- Etc.

Additionally having a concrete example makes it easier in architecture
discussion as this lays the groundwork for a service with clear boundaries and
contracts. Often architecture discussions that don't have concrete examples can
go off of the cliff into "What If" land, making this a simple way to communicate
my vision of building out common python services

## Assumptions

- Uses a verbose response spec [HAL](https://github.com/mikekelly/hal_specification)
- Relies on a MySQL Database database as a datastore ([database tradeoffs](#database-tradeoffs))
- Handles requirements within the `setup.py` file, production values frozen into
requirements.txt

## Install

```bash
$ make install
```

## Easy local development

```bash
$ docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql
$ docker build -t app .
$ docker run --name app --link some-mysql:mysql -d app
```

## Database Tradeoffs

AKA Why MySQL.

For this project I chose MySQL for a few reasons.

These days most simplistic services have data that is relational, especially
with the goal for this repo to serve as a blueprint for new development. This
will easily solve common services needed for a new ecosystem: user management,
business logic service layer, etc..

Additionally MySQL can be handled simplisticly at first, allowing us to focus on
the functionality over the infrastructure. Both Google Cloud and AWS offer
hosted MySQL, continuing the focus on functionality over infrastructure. As well
as the more long term handling of multi-region support through Aurora. While
PostgreSQL is also an option (as of writing this) Google Cloud only supports
this in a beta fashion making it less of production support.

### Why Not MongoDB

All web-scale jokes aside, MongoDB can be used successfully as a data store. The
piece that is looked over is whether you are building out a service that cares
more about documents versus relational data, as this should be the main
indicator of the SQL for No-SQL data store. Though I'll leave the long winded
debates to the top hits on google, this is my simplistic rule of thumb.

### Why Not A Hosted Solution

Other arguments I've heard are using something like DynamoDB to allow AWS to
truly scale this out as necessary. While I believe this to be a successful
project the work I've done with it narrows it down to be more of a key-value
store than a relational (or even document) datastore. The difference can be
subtle but some thuoght experiments can suss out whether a key-value store is
really useful for your data. As any datastore *can* be used doesn't mean that
they will help you get your solutoin out quickly, with the opportunity to
iterate on your product into tooling that might be better suited.

I don't have enough experience to omment on a number of other cloud hosted
solutoin but feel more strongly that using something you know while you are
still starting out and transitioning to something that might be the better tool
later is a way to better ensure quick progress early on.
