
![logo](https://raw.githubusercontent.com/Lemaf/spo/master/img/logo.png)

### System Paths Organizer

Script standardization of file and folder,paths. The script checks the current date and organizes backups of folders and releases according to the date prior to the current day (**without compromising the work**), and generating log in ``/var/log/orgfolders/orgfolders.log``. 

---

#### Usage:

python spo **service** path

**Example**:
```
python spo sicar /var/play
```
or help command:

```
python spo.py --help
```



---

#### Release v.0.1.0 features:
* Make and move release files in releases path. 
* Make and move old files in backup path.
* Generating log file.

---

#### Contact:
* vitor.lobo@lemaf.ufla.br
* lobocode@fedoraproject.org

