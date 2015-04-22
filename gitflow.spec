Name:       gitflow
Version:    0.4.2
Release:    1%{?dist}
Summary:    Extensions providing operations for V. Driessen's branching model

Group:      Development/Languages
License:    BSD
URL:        https://github.com/nvie/gitflow
# You can get this tarball by cloning the repository from github and checking
# out revision %%{githash}
Source0:    gitflow-0.4.2.tar.gz
# There is no upstream ticket for this patch, but instead just hardcodes the
# directory we're installing to for Fedora.
Patch0:     gitflow-Appropriate-GITFLOW_DIR.patch

BuildArch:  noarch

Requires:       shflags
Requires:       git

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
A collection of Git extensions to provide high-level repository operations
for Vincent Driessen's [branching model](http://nvie.com/git-model "original
blog post").

For the best introduction to get started with `git flow`, please read Jeff
Kreeftmeijer's blog post:

  http://jeffkreeftmeijer.com/2010/why-arent-you-using-git-flow/

Or have a look at one of these screen casts:

* [A short introduction to git-flow]
  (http://vimeo.com/16018419) (by Mark Derricutt)
* [On the path with git-flow]
  (http://codesherpas.com/screencasts/on_the_path_gitflow.mov) (by Dave Bock)

%prep
%setup -q -n %{name}
%patch0 -p1 -b .gitflowdir

%build
# This section is empty because this package ccontains shell scripts
# to be sourced: there's nothing to build

%install
mkdir -p %{buildroot}/%{_bindir}
install -v -m 0755 git-flow %{buildroot}/%{_bindir}

mkdir -p %{buildroot}/%{_datadir}/%{name}
install -v -m 0644 git-flow-init %{buildroot}/%{_datadir}/%{name}
install -v -m 0644 git-flow-feature %{buildroot}/%{_datadir}/%{name}
install -v -m 0644 git-flow-hotfix %{buildroot}/%{_datadir}/%{name}
install -v -m 0644 git-flow-release %{buildroot}/%{_datadir}/%{name}
install -v -m 0644 git-flow-support %{buildroot}/%{_datadir}/%{name}
install -v -m 0644 git-flow-version %{buildroot}/%{_datadir}/%{name}
install -v -m 0644 gitflow-common %{buildroot}/%{_datadir}/%{name}

ln -s %{_datadir}/shflags/shflags %{buildroot}/%{_datadir}/%{name}/gitflow-shFlags

%files
%doc README.mdown LICENSE AUTHORS Changes.mdown
%{_bindir}/git-flow*
%{_datadir}/%{name}

%changelog
* Mon Jul 23 2012 Ralph Bean <rbean@redhat.com> - 0.4.2.20120723git53e9c76-1
- New checkout from upstream git for review process.

* Mon Jul 23 2012 Ralph Bean <rbean@redhat.com> - 0.4.2.20120626gitab7fda2-2
- Changed License field to BSD
- Dropped requirement on util-linux.
- Added comments for Source0 and Patch0
- Using macro for %%{gitdate} as well as %%{githash}

* Tue Jun 26 2012 Ralph Bean <rbean@redhat.com> - 0.4.2.20120626gitab7fda2-1
- Initial packaging for Fedora.
